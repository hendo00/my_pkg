cmake_minimum_required(VERSION 3.8)
project(my_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)

set(dependencies
rclcpp
std_msgs
sensor_msgs)

set(simple_sources
src/publisher.cpp
src/subscriber.cpp
src/simple.cpp)

set(logging_sources
src/logging.cpp)

set(logging_class_sources
src/logger_class.cpp)

# set(pub_class_sources
# src/publisher.cpp)

# set(sub_class_sources
# src/subscriber.cpp)

set(param_sources
src/param_reader.cpp)

include_directories(
  include
)

add_executable(logging ${logging_sources})
add_executable(logger_class ${logging_class_sources})
add_executable(simple ${simple_sources})
#add_executable(publisher ${pub_class_sources})
#add_executable(subscriber ${sub_class_sources})
add_executable(param_reader ${param_sources})

ament_target_dependencies(simple ${dependencies})
ament_target_dependencies(logging ${dependencies})
ament_target_dependencies(logger_class ${dependencies})
# ament_target_dependencies(publisher ${dependencies})
# ament_target_dependencies(subscriber ${dependencies})
ament_target_dependencies(param_reader ${dependencies})


install(TARGETS
simple
logging
logger_class
# publisher
# subscriber
param_reader
ARCHIVE DESTINATION lib
LIBRARY DESTINATION lib
RUNTIME DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY launch config worlds description DESTINATION share/${PROJECT_NAME})
install(
  DIRECTORY include
  DESTINATION include
)
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()
ament_export_include_directories(include)
ament_export_dependencies(${dependencies})
ament_package()
