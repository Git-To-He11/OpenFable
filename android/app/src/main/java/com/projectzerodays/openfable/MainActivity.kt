package com.projectzerodays.openfable

import android.Manifest
import android.content.pm.PackageManager
import android.os.Build
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.core.app.ActivityCompat
import com.projectzerodays.openfable.ui.ClassificationFrame
import com.projectzerodays.openfable.ui.ClassificationRed
import com.projectzerodays.openfable.ui.QuantumUi
import com.projectzerodays.openfable.ui.theme.QuantumTheme

class MainActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // System bars match the classification banner — the marking runs edge to edge.
        window.statusBarColor = android.graphics.Color.rgb(0x8B, 0x1A, 0x1A)
        window.navigationBarColor = android.graphics.Color.rgb(0x8B, 0x1A, 0x1A)
        requestNotificationPermissionIfNeeded()
        requestStoragePermissionIfNeeded()
        setContent {
            QuantumTheme {
                ClassificationFrame { QuantumUi() }
            }
        }
    }

    private fun requestNotificationPermissionIfNeeded() {
        if (Build.VERSION.SDK_INT >= 33 &&
            checkSelfPermission(Manifest.permission.POST_NOTIFICATIONS) !=
            PackageManager.PERMISSION_GRANTED
        ) {
            ActivityCompat.requestPermissions(
                this,
                arrayOf(Manifest.permission.POST_NOTIFICATIONS),
                1001
            )
        }
    }

    private fun requestStoragePermissionIfNeeded() {
        val storagePermissions = if (Build.VERSION.SDK_INT >= 33) {
            arrayOf(Manifest.permission.READ_EXTERNAL_STORAGE, Manifest.permission.WRITE_EXTERNAL_STORAGE)
        } else {
            arrayOf(
                Manifest.permission.READ_EXTERNAL_STORAGE,
                Manifest.permission.WRITE_EXTERNAL_STORAGE
            )
        }
        val needed = storagePermissions.filter {
            checkSelfPermission(it) != PackageManager.PERMISSION_GRANTED
        }.toTypedArray()
        if (needed.isNotEmpty()) {
            ActivityCompat.requestPermissions(
                this,
                needed,
                1002
            )
        }
    }
}
