# Raspberry PiのセットアップからPython環境のインストールまで

## はじめに

`Mac環境の記事ですが、Windows環境も同じ手順になります。環境依存の部分は読み替えてお試しください。`

### 目的

この記事を最後まで読むと、次のことができるようになります。

| No.  | 概要                   | キーワード      |
| :--- | :--------------------- | :-------------- |
| 1    | OSインストール         | Raspberry Pi OS |
| 2    | Wi-FiステルスSSID設定  |                 |
| 3    | 固定IPアドレス設定     |                 |
| 4    | SSH接続                |                 |
| 5    | VNC接続                |                 |
| 6    | Python環境インストール | pyenv           |

### 実行環境

| 環境                       | Ver.    |
| :------------------------- | :------ |
| macOS Catalina             | 10.15.6 |
| Raspberry Pi OS (Raspbian) | 10      |
| Raspberry Pi Imager        | 1.4     |
| pyenv                      | 1.2.20  |
| Python                     | 3.7.3   |

### 関連する記事

- [Raspberry Pi](https://www.raspberrypi.org/)
- [pyenv](https://github.com/pyenv/pyenv)

## 1. OSインストール

### SDカード確認(macOS)

```command.sh
~% diskutil list

/dev/disk0 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
...

/dev/disk1 (synthesized):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
...

/dev/disk2 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *31.9 GB    disk2
   1:             Windows_FAT_32 boot                    268.4 MB   disk2s1
   2:                      Linux                         31.6 GB    disk2s2
```

### SDカード初期化(macOS)

```command.sh
~% diskutil eraseDisk FAT32 RPI /dev/disk2
```

### Raspberry Pi Imagerインストール(macOS)

```command.sh
~% brew cask install raspberry-pi-imager
```

### インストール

1. Raspberry Pi Imager起動 > OSイメージ選択 > SDカード選択 > WRITE

## 2. Wi-FiステルスSSID設定

### パスワード暗号化

```command.sh
~$ wpa_passphrase {ssid} {password}

network={
    ssid="{ssid}"
    #psk="{password}"
    psk={psk}
}
```

### Wi-Fi設定

```command.sh
~$ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

```command.sh
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=JP

+ network={
+     ssid="{ssid}"
+     scan_ssid=1
+     psk={psk}
+ }
```

```command.sh
^O
^X
```

```command.sh
~$ sudo reboot
```

## 3. 固定IPアドレス設定

### デフォルトゲートウェイ確認(macOS)

```command.sh
~% netstat -rn

Routing tables

Internet:
Destination        Gateway            Flags        Netif Expire
default            {default gateway}  UGSc         en0
...
```

### DNSサーバー確認(macOS)

```command.sh
~% cat /etc/resolv.conf

nameserver {primary dns}
nameserver {secondary dns}
```

### IPアドレス設定

```command.sh
~$ sudo nano /etc/dhcpcd.conf
```

```command.sh
# fallback to static profile on eth0
#interface eth0
#fallback static_eth0

+ interface wlan0
+ static ip_address={ip address}/24
+ static routers={default gateway}
+ static domain_name_servers={primary dns}
+ static domain_search=
```

```command.sh
^O
^X
```

```command.sh
~$ sudo reboot
```

## 4. SSH接続

### SSH有効設定

```command.sh
~$ sudo touch /boot/ssh
```

### SSHホスト鍵削除(macOS)

```command.sh
~% ssh-keygen -R {ip address}
~% ssh-keygen -R raspberrypi.local
```

### SSH接続(macOS)

```command.sh
~% ssh pi@{ip address}
```

```command.sh
~% ssh pi@raspberrypi.local
```

## 5. VNC接続

### VNCインストール

```command.sh
~$ sudo apt-get update
~$ sudo apt-get upgrade
~$ sudo apt-get install tightvncserver
```

### VNC起動

```command.sh
~$ tightvncserver
```

### VNC接続(macOS)

1. Finder > 移動 > サーバへ接続
2. `vnc://{ip address}:5901` or `vnc://raspberrypi.local:5901`入力 > 接続

## 6. Python環境インストール

### ライブラリインストール

```command.sh
~$ sudo apt update
~$ sudo apt upgrade
~$ sudo apt install -y git openssl libssl-dev libbz2-dev libreadline-dev libsqlite3-dev libffi-dev
```

### pyenvインストール

```command.sh
~$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
~$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
~$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
~$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
~$ source ~/.bash_profile
```

### Pythonインストール

```command.sh
~$ pyenv install -l
```

```command.sh
~$ pyenv install {version}
```

### Python切り替え

```command.sh
~$ pyenv global {version}
```
