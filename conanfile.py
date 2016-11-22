from conans import ConanFile, CMake

class GlenniferClientConan(ConanFile):
   name = "amqp"
   version = "1.0-snapshot"
   url = "https://github.com/cwruRobotics/amqpcpp.git"
   license = "MIT"
   exports = "examples*", "include*", "src*", "CMakeLists.txt"
   settings = "os", "compiler", "build_type", "arch"
   requires = "librabbitmq/0.8.1@filonovpv/stable"
   generators = "cmake"
   build_policy = "missing"
   default_options = "librabbitmq:no_openssl=True"

   def build(self):
      cmake = CMake(self.settings)
      self.run('cmake %s %s' % (self.conanfile_directory, cmake.command_line))
      self.run("cmake --build . %s" % cmake.build_config)

   def package(self):
      self.copy("*.h", dst=".")
      self.copy("*.lib", dst="lib", src="lib")
      self.copy("*.a", dst="lib", src="lib")
      self.copy("*.so", dst="lib", src="lib")
      self.copy("*.dll", dst="bin", src="lib")
      self.copy("*.dll", dst="bin", src="bin")

   def package_info(self):
      self.cpp_info.libs = ["amqp"]