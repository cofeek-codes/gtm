set -xe

pyinstaller main.py -F

rm -rf build/ main.spec

cp ./binaries/ dist/binaries/ -r
