cmake_minimum_required (VERSION 2.6)
project (AMQP)
include_directories("include")
add_library(AMQP src/AMQP.cpp src/AMQPBase.cpp src/AMQPException.cpp src/AMQPExchange.cpp src/AMQPMessage.cpp src/AMQPQueue.cpp)