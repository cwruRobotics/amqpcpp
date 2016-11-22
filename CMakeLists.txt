cmake_minimum_required (VERSION 2.6)
include (GenerateExportHeader)
project (AMQP)

include_directories("include")

include(conanbuildinfo.cmake)
conan_basic_setup()

add_library(AMQP SHARED src/AMQP.cpp src/AMQPBase.cpp src/AMQPException.cpp src/AMQPExchange.cpp src/AMQPMessage.cpp src/AMQPQueue.cpp)
target_link_libraries(AMQP ${CONAN_LIBS})

add_executable(ExampleConsume examples/example_consume.cpp)
target_link_libraries(ExampleConsume AMQP ${CONAN_LIBS})

add_executable(ExamplePublish examples/example_publish.cpp)
target_link_libraries(ExamplePublish AMQP ${CONAN_LIBS})

add_executable(ExampleGet examples/example_get.cpp)
target_link_libraries(ExampleGet AMQP ${CONAN_LIBS})
