cmake_minimum_required(VERSION 3.6)
project(instruments)
INCLUDE_DIRECTORIES(include，
        "/Library/Frameworks/VISA.framework/Versions/A/Headers")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main.cpp remote.cpp interface.h interface.cpp)
add_executable(instruments ${SOURCE_FILES})
target_link_libraries (instruments /library/frameworks/VISA.framework)



