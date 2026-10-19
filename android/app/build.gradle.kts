import java.util.Properties

plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
    id("org.jetbrains.kotlin.plugin.compose") version "2.1.0"
}

// ---------------------------------------------------------------------------
// Release signing from environment variables (CI + local release builds):
//   OPENFABLE_KEYSTORE           path to the keystore (.jks)
//   OPENFABLE_KEYSTORE_PASSWORD  keystore password
//   OPENFABLE_KEY_ALIAS          key alias
//   OPENFABLE_KEY_PASSWORD       key password (defaults to keystore password)
// Falls back to debug signing when the variables are absent so local
// `assembleRelease` still produces an installable APK.
// ---------------------------------------------------------------------------
val envKeystore: String? = providers.environmentVariable("OPENFABLE_KEYSTORE").orNull
val envStorePass: String? = providers.environmentVariable("OPENFABLE_KEYSTORE_PASSWORD").orNull
val envKeyAlias: String? = providers.environmentVariable("OPENFABLE_KEY_ALIAS").orNull
val envKeyPass: String? = providers.environmentVariable("OPENFABLE_KEY_PASSWORD").orNull ?: envStorePass

android {
    namespace = "com.projectzerodays.openfable"
    compileSdk = 35

    defaultConfig {
        applicationId = "com.projectzerodays.openfable"
        minSdk = 26
        targetSdk = 35
        versionCode = 5
        versionName = "0.2.0"
        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
        vectorDrawables { useSupportLibrary = true }
    }

    signingConfigs {
        if (envKeystore != null && envStorePass != null && envKeyAlias != null && envKeyPass != null) {
            create("release") {
                storeFile = rootProject.file(envKeystore).takeIf { it.isAbsolute }
                    ?: file(envKeystore)
                storePassword = envStorePass
                keyAlias = envKeyAlias
                keyPassword = envKeyPass
                enableV1Signing = true
                enableV2Signing = true
                enableV3Signing = true
            }
        } else {
            // Allow local release builds with debug key for testing
            create("release") {
                storeFile = rootProject.file("debug.keystore")
                storePassword = "android"
                keyAlias = "androiddebugkey"
                keyPassword = "android"
                enableV1Signing = true
                enableV2Signing = true
                enableV3Signing = true
            }
        }
    }

    buildTypes {
        release {
            isMinifyEnabled = true
            isShrinkResources = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
            signingConfig = signingConfigs.getByName("release")
        }
        debug {
            applicationIdSuffix = ".debug"
        }
    }

    // 'full'    — root-enabled build: privileged operations (footprint wipe,
    //             persistence hardening) go through `su`.
    // 'limited' — no-root build: standard app permissions only.
    flavorDimensions += "mode"
    productFlavors {
        create("full") {
            dimension = "mode"
            applicationIdSuffix = ".full"
            versionNameSuffix = "-full"
            buildConfigField("boolean", "ROOT_CAPABLE", "true")
        }
        create("limited") {
            dimension = "mode"
            applicationIdSuffix = ".limited"
            versionNameSuffix = "-limited"
            buildConfigField("boolean", "ROOT_CAPABLE", "false")
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    kotlinOptions {
        jvmTarget = "17"
    }
    buildFeatures {
        compose = true
        buildConfig = true
    }
    composeOptions {
        // Kotlin 2.0+ uses the Compose Compiler Gradle plugin instead of kotlinCompilerExtensionVersion
    }
    packaging {
        resources {
            excludes += "/META-INF/{AL2.0,LGPL2.1}"
            excludes += "/META-INF/INDEX.LIST"
            excludes += "/META-INF/DEPENDENCIES"
            excludes += "META-INF/versions/9/OSGI-INF/MANIFEST.MF"
        }
    }
    lint {
        abortOnError = true
        checkReleaseBuilds = true
    }
    testOptions {
        unitTests.isReturnDefaultValues = true
    }
}

dependencies {
    val composeBom = platform("androidx.compose:compose-bom:2024.10.01")
    implementation(composeBom)
    androidTestImplementation(composeBom)

    implementation("androidx.core:core-ktx:1.13.1")
    implementation("androidx.lifecycle:lifecycle-runtime-ktx:2.8.4")
    implementation("androidx.lifecycle:lifecycle-viewmodel-compose:2.8.4")
    implementation("androidx.activity:activity-compose:1.9.1")
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.8.1")

    implementation("androidx.compose.ui:ui")
    implementation("androidx.compose.ui:ui-graphics")
    implementation("androidx.compose.ui:ui-tooling-preview")
    implementation("androidx.compose.material3:material3")
    implementation("androidx.compose.material:material-icons-extended")
    debugImplementation("androidx.compose.ui:ui-tooling")

    // C2 HTTP server (embedded, ~100 KB jar — lighter than Ktor for on-device serving)
    implementation("org.nanohttpd:nanohttpd:2.3.1")

    // Local on-device LLM inference (MediaPipe GenAI .task models)
    implementation("com.google.mediapipe:tasks-genai:0.10.14")

    // Encrypted storage for the AI API key
    implementation("androidx.security:security-crypto:1.0.0")
    // Dadb — pure-Kotlin ADB client (no adb binary needed)
    // Its POM drags junit-platform-native (runtime scope) which pulls the whole
    // JUnit 5 suite into the APK and collides on META-INF/LICENSE.md — exclude.
    implementation("dev.mobile:dadb:1.2.9") {
        exclude(group = "org.graalvm.buildtools")
        exclude(group = "org.junit.jupiter")
        exclude(group = "org.junit.platform")
    }

    testImplementation("junit:junit:4.13.2")
    // real org.json on the JVM test classpath (android.jar stubs no-op it)
    testImplementation("org.json:json:20240303")
    androidTestImplementation("androidx.test.ext:junit:1.2.1")
    androidTestImplementation("androidx.test.espresso:espresso-core:3.6.1")
    androidTestImplementation("androidx.compose.ui:ui-test-junit4")
}
