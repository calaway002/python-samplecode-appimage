# python-samplecode-appimage
sample code for create the appimage using python code and some basic png
my_python_app/
├── main.py
└── myicon.png

AppDir/
├── AppRun
├── myicon.png
└── usr/
    ├── bin/
    └── share/
        └── icons/
            └── hicolor/
                └── 256x256/
                    └── apps/
                        └── myicon.png


appimage-builder --recipe appimage-builder.yml
