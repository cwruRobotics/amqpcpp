from conans import ConanFile

class GlenniferClientConan(ConanFile):
   settings = "os", "compiler", "build_type", "arch"
   requires = "librabbitmq/0.8.1@filonovpv/stable"
   generators = "cmake"
   build_policy = "missing"
   default_options = "librabbitmq:no_openssl=True"
