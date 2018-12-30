from conans import ConanFile, tools, Meson
import os

class DataframeConan(ConanFile):
    name = "net_example01"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "pkg_config"
    # exports_sources = "src/*"
    requires = (
        "boost/1.69.0@conan/stable"
    )

    def build(self):
        meson = Meson(self)
        meson.configure()
        meson.build()
