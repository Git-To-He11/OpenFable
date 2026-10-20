# Quantum2 Technical Specification

## Overview

Quantum2 is a cyber warfare framework that provides REST API and WebSocket endpoints for zero-click exploits and APT toolkits. The framework is designed for advanced penetration testing and red team operations.

## API Endpoints

### Zero-Click Exploits

#### List Zero-Click Exploits
- **Endpoint**: `GET /api/exploits/zeroclick/list`
- **Description**: Lists all available zero-click exploits categorized by attack vector
- **Response**:
  ```json
  {
    "imessage": ["ForceEntry", "BlastPass", "Triangulation", "CoreAudioExploit", "NickName"],
    "bluetooth": ["BleedingTooth", "BlueFrag", "BlueBorne"],
    "web": ["WebRender", "WebKitExploit", "WebRTCZeroClick"],
    "wifi": ["KR06", "BroadcomWiFi"],
    "kernel": ["LinuxBluetooth", "WindowsBluetooth"],
    "hardware": ["NFCRelay", "NFCInjection", "BadUSB", "USBMassStorage"]
  }
  ```

#### Execute Zero-Click Exploit
- **Endpoint**: `POST /api/exploits/zeroclick/execute`
- **Description**: Executes a zero-click exploit against a target
- **Request Body**:
  ```json
  {
    "target": "string",
    "protocol": "string",
    "payload": "string (hex encoded)",
    "apt_group": "string"
  }
  ```
- **Response**:
  ```json
  {
    "job_id": "string",
    "status": "string",
    "result": "object"
  }
  ```

#### Get Exploit Result
- **Endpoint**: `GET /api/exploits/zeroclick/{job_id}`
- **Description**: Retrieves the result of an exploit execution
- **Response**: Exploit execution result object

### APT Toolkits

#### List APT Groups
- **Endpoint**: `GET /api/apts/list`
- **Description**: Lists all available APT toolkits
- **Response**:
  ```json
  {
    "apt_groups": {
      "nso": ["Pegasus", "MILLYMOUSE", "MILLICLEAN", "JEDGROPE"],
      "nsa": ["QUANTUM", "TAO", "TURBINE"],
      "apt28": ["SofacyLoader", "XAgent"],
      "apt29": ["CozyBear", "TheMoscow"],
      "apt31": ["JudgmentPanda", "Hikit"],
      "apt37": ["Scarcat", "Kerrigan"],
      "apt41": ["Barium", "WickedPanda"],
      "financial": ["FIN7", "Carbanak", "LazarusGroup"]
    },
    "eternal_exploits": ["EternalBlue", "EternalRed", "EternalChampion", "EternalRomance"]
  }
  ```

#### Build APT Tool
- **Endpoint**: `POST /api/apts/build/{tool_name}`
- **Description**: Builds configuration for a specific APT tool
- **Request Body**:
  ```json
  {
    "target": "string"
  }
  ```
- **Response**: Tool configuration object

#### List NSA Tools
- **Endpoint**: `GET /api/nsa/tools`
- **Description**: Lists NSA TAO tools and Eternal exploits
- **Response**:
  ```json
  {
    "tools": {
      "QUANTUM": "Network injection system",
      "TAO_TOOLKIT": "Tailored Access Operations toolkit",
      "TURBINE": "Botnet command infrastructure",
      "IMPACT": "Post-exploitation framework",
      "CLEANFLOPPY": "Disk wiping utility",
      "QUANTUMINSERT": "Man-in-the-middle injection",
      "LEVERAGE": "Exploitation framework",
      "VALIDIADICTOR": "Validation framework",
      "METHSTIC": "Network monitoring tool"
    },
    "eternal_exploits": {
      "EternalBlue": {
        "cve": "CVE-2017-0144",
        "target": "Windows SMBv1",
        "platform": "Windows",
        "ms_plat": "MS17-010"
      }
    }
  }
  ```

#### Get Eternal Exploit Details
- **Endpoint**: `GET /api/nsa/eternal/{exploit_name}`
- **Description**: Gets detailed information about an Eternal exploit
- **Response**: Eternal exploit details object

### Payloads

#### List Payload Types
- **Endpoint**: `GET /api/payloads/types`
- **Description**: Lists available payload types
- **Response**:
  ```json
  {
    "payloads": [
      {"type": "windows/x64/meterpreter", "category": "windows"},
      {"type": "linux/x64/reverse_shell", "category": "linux"},
      {"type": "macos/arm64/reverse_shell", "category": "macos"},
      {"type": "webshell/php", "category": "web"},
      {"type": "zeroclick/imessage", "category": "zeroclick"},
      {"type": "dropper/windows", "category": "windows"}
    ]
  }
  ```

#### Generate Payload
- **Endpoint**: `POST /api/payloads/generate`
- **Description**: Generates a payload
- **Request Body**:
  ```json
  {
    "exploit_type": "string",
    "target": "string",
    "payload_data": "string"
  }
  ```
- **Response**:
  ```json
  {
    "payload_type": "string",
    "target": "string",
    "payload": "string",
    "size": "integer",
    "encryption": "string",
    "evasion": ["string"]
  }
  ```

### Primitives

#### List Primitives
- **Endpoint**: `GET /api/primitives/list`
- **Description**: Lists memory corruption primitives
- **Response**:
  ```json
  {
    "primitives": [
      {"name": "Type Confusion", "type": "type_confusion", "capabilities": ["read", "write"]},
      {"name": "Heap Overflow", "type": "heap_buffer_overflow", "capabilities": ["write"]},
      {"name": "Use-After-Free", "type": "use_after_free", "capabilities": ["read", "write", "spray"]},
      {"name": "Integer Overflow", "type": "integer_overflow", "capabilities": ["write"]},
      {"name": "Stack Overflow", "type": "stack_overflow", "capabilities": ["rip_control"]}
    ]
  }
  ```

#### Build Primitive
- **Endpoint**: `POST /api/primitives/build`
- **Description**: Builds a memory corruption primitive
- **Request Body**:
  ```json
  {
    "primitive_type": "string",
    "platform": "string"
  }
  ```
- **Response**: Primitive object

### Delivery

#### Covert Channel Encoding
- **Endpoint**: `GET /api/delivery/covert/{channel}`
- **Description**: Encodes data for covert channel transmission
- **Parameters**: 
  - `channel`: dns, http, websocket, or image
  - `data`: string to encode
- **Response**:
  ```json
  {
    "channel": "string",
    "encoded": "string"
  }
  ```

### Operations

#### List Operations
- **Endpoint**: `GET /api/operations`
- **Description**: Lists ongoing operations
- **Response**:
  ```json
  {
    "operations": [
      {"id": "OP-001", "name": "Triangulation Campaign", "status": "active", "targets": 42},
      {"id": "OP-002", "name": "BlueFrag Scan", "status": "running", "targets": 128},
      {"id": "OP-003", "name": "NSA TAO", "status": "active", "targets": 7}
    ]
  }
  ```

#### Create Operation
- **Endpoint**: `POST /api/operations/create`
- **Description**: Creates a new operation
- **Request Body**:
  ```json
  {
    "name": "string",
    "target": "string",
    "method": "string"
  }
  ```
- **Response**:
  ```json
  {
    "job_id": "string",
    "status": "string",
    "operation": "string"
  }
  ```

#### Get Operation Details
- **Endpoint**: `GET /api/operations/{operation_id}`
- **Description**: Gets detailed information about an operation
- **Response**: Operation details object

### Dashboard

#### Get Dashboard Statistics
- **Endpoint**: `GET /api/dashboard/stats`
- **Description**: Gets dashboard statistics
- **Response**:
  ```json
  {
    "active_operations": "integer",
    "zero_click_exploits": "integer",
    "apt_tools": "integer",
    "delivered_payloads": "integer",
    "active_agents": "integer",
    "detected_threats": "integer",
    "blocked_attacks": "integer",
    "recent_events": [
      {"timestamp": "float", "event": "string", "severity": "string"}
    ]
  }
  ```

#### Get Targets
- **Endpoint**: `GET /api/dashboard/targets`
- **Description**: Gets list of targets
- **Response**:
  ```json
  {
    "targets": [
      {"id": "TGT-001", "hostname": "string", "ip": "string", "status": "string"},
      {"id": "TGT-002", "hostname": "string", "ip": "string", "status": "string"},
      {"id": "TGT-003", "hostname": "string", "ip": "string", "status": "string"}
    ]
  }
  ```

## WebSocket Endpoints

### Exploit Status Updates
- **Endpoint**: `WebSocket /ws/exploits`
- **Description**: WebSocket connection for receiving exploit status updates

### Operation Updates
- **Endpoint**: `WebSocket /ws/operations`
- **Description**: WebSocket connection for receiving operation updates

## Data Models

### ExploitRequest
```python
class ExploitRequest(BaseModel):
    target: str = ""
    protocol: str = "auto"
    payload: Optional[str] = None
    apt_group: Optional[str] = None
```

### PayloadRequest
```python
class PayloadRequest(BaseModel):
    exploit_type: str
    target: str
    payload_data: Optional[str] = None
```

### PrimitiveRequest
```python
class PrimitiveRequest(BaseModel):
    primitive_type: str
    platform: str = "auto"
```

### OperationRequest
```python
class OperationRequest(BaseModel):
    name: str
    target: str
    method: str = "zeroclick"
```

### APTBuildRequest
```python
class APTBuildRequest(BaseModel):
    target: str = ""
```

## Security Features

### Zero-Click Exploits
The framework includes several zero-click exploit implementations:

1. **iMessage Exploits**:
   - ForceEntry (CVE-2021-30860)
   - BlastPass (CVE-2022-32932)
   - Triangulation
   - CoreAudioExploit (CVE-2025-31200)
   - NickName

2. **Bluetooth Exploits**:
   - BleedingTooth (CVE-2020-12351)
   - BlueFrag (CVE-2020-0022)
   - BlueBorne (CVE-2017-0781)

3. **Web Exploits**:
   - WebKitExploit (CVE-2023-32346)
   - WebRender (CVE-2023-2958)
   - WebRTCZeroClick (CVE-2023-5217)

4. **WiFi Exploits**:
   - KR06 (CVE-2023-2067)
   - BroadcomWiFi (CVE-2019-1563)

5. **Kernel Exploits**:
   - LinuxBluetooth
   - WindowsBluetooth

6. **Hardware Exploits**:
   - NFCRelay
   - NFCInjection
   - BadUSB
   - USBMassStorage

### APT Toolkits
The framework includes implementations of various APT group toolkits:

1. **NSO Group**:
   - Pegasus: iOS/macOS surveillanceware
   - MILLYMOUSE: Windows/Linux loader
   - MILLICLEAN: Windows rootkit
   - JEDGROPE: iOS post-exploitation

2. **NSA/TAO**:
   - QUANTUM: Network injection system
   - TAO: Tailored Access Operations toolkit
   - TURBINE: Botnet command infrastructure

3. **APT28 (Fancy Bear)**:
   - SofacyLoader: Office macro-based loader
   - XAgent: Full-featured RAT

### Memory Corruption Primitives
The framework provides several memory corruption primitives for exploit development:

1. **Type Confusion**: Allows arbitrary read/write via JavaScriptCore type confusion
2. **Heap Overflow**: Controlled heap overflow with configurable size
3. **Use-After-Free**: UAF via crafted object lifecycle
4. **Integer Overflow**: Signed integer overflow to controlled value
5. **Stack Overflow**: Stack buffer overflow with return address control

### Covert Channels
The framework supports multiple covert communication channels:
1. **DNS**: Encodes data in DNS queries
2. **HTTP Headers**: Encodes data in HTTP headers
3. **WebSocket**: Encodes data in WebSocket frames
4. **Image Steganography**: Embeds data in image files

### Encryption and Evasion
- Payloads are encrypted with AES-256-GCM
- Anti-sandbox, anti-EDR, and memory-only evasion techniques
- Persistence mechanisms for long-term access