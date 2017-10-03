TEMPLATE = aux
OTHER_FILES = \
        diff/ \
        patch/ \
        rpm/ \
        src/

src.path = /var/lib/environment/compositor

patch.files = patch/*
patch.path = /usr/share/patchmanager/patches/disable-kalman-filter-inoir7

original = original$${src.path}/droid-hal-device.conf
patched = patched$${src.path}/droid-hal-device.conf

system((cd diff; diff -uprN $$original $$patched) > patch/unified_diff.patch)

INSTALLS += \
        src \
        patch
