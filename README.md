# moonshine-speech-server
Project demonstrating running Moonshine's ASR models as a web API

```bash
# See https://repost.aws/knowledge-center/ec2-memory-swap-file
sudo dd if=/dev/zero of=/swapfile bs=128M count=32
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
sudo swapon -s
# Should show the new swap volume.
echo "/swapfile swap swap defaults 0 0" | sudo tee --append '/etc/fstab'

sudo yum install -y git pip

git clone https://github.com/moonshine-ai/moonshine-speech-server

pip install useful-moonshine-onnx@git+https://git@github.com/usefulsensors/moonshine.git#subdirectory=moonshine-onnx

python moonshine-speech-server/test.py
```
