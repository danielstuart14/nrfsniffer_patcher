# nRF BLE Sniffer Patcher (LDO Boards)

This repository contains a simple python script that can patch any `.hex` image with a patch file.  
It is being used to patch Nordic's BLE Sniffer firmware to enable LDO-only nRF52840 boards to work with it.

Currently, only `sniffer_nrf52840dongle_nrf52840_4.1.1.hex` firmware is supported, mostly targeting the Holyiot 22046 dongle (but should work with any nRF52840 board that exposes its USB).

### How to use it
1. Download / clone this repository
2. Download the sniffer firmware from [Nordic's website](https://www.nordicsemi.com/Products/Development-tools/nRF-Sniffer-for-Bluetooth-LE/Download?lang=en#infotabs).
3. Copy the `sniffer_nrf52840dongle_nrf52840_4.1.1.hex` file to the directory where you downloaded / cloned this repository.
4. Run the patcher:  
    ```$ python patch.py sniffer_nrf52840dongle_nrf52840_4.1.1.patch sniffer_nrf52840dongle_nrf52840_4.1.1.hex patched_sniffer.hex```
5. Flash the `patched_sniffer.hex`with Nordic's nRF Connect for Desktop (Programmer App)
    - For Holyiot 22046 dongle, you can enter bootloader mode by holding its button for a couple seconds.

### Sniffing with Wireshark
1. Install [Wireshark](https://www.wireshark.org/download.html)
2. Copy the `extcap` folder from the Nordic's `nrf_sniffer_for_bluetooth_le_4.1.1.zip` you downloaded to the folder where Wireshark was installed (if asked, allow for files to be overwritten and folders to be merged)
    - On Windows it is installed by default at: `C:\Program Files\Wireshark`
3. Copy the `Profile_nRF_Sniffer_Bluetooth_LE` folder from the zip to the Wireshark `profiles` folder
    - On Windows it would be: `C:\Program Files\Wireshark\profiles`
4. Open Wireshark and change the profile (At the bottom right of the window) to the nRF one.
5. Double click the nRF Sniffer on the capture list and you should start to see packets being sniffed.
    - You can find more information at [Nordic's infocenter](https://infocenter.nordicsemi.com/topic/ug_sniffer_ble/UG/sniffer_ble/sniffer_usage.html).
