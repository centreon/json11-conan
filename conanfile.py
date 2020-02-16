from conans import ConanFile, CMake, tools


class Json11Conan(ConanFile):
    name = "json11"
    version = "e2e3a11"
    changelist = "e2e3a11e99672b018e0e0657867e6a3439e180cf"
    license = "MIT License"
    author = "Sylvestre Gallon <ccna.syl@gmail.com>"
    url = "https://github.com/dropbox/json11"
    description = "A small json c++11 library"
    topics = ("json", "c++11")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/dropbox/json11")
        # This small hack might be useful to guarantee proper /MT /MD linkage
        # in MSVC if the packaged project doesn't have variables to set it
        # properly
        tools.replace_in_file("json11/CMakeLists.txt", "enable_testing()",
                              '''enable_testing()
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="json11")
        cmake.build()

    def package(self):
        self.copy("*.hpp", dst="include", src="json11")
        self.copy("*json11.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["json11"]

