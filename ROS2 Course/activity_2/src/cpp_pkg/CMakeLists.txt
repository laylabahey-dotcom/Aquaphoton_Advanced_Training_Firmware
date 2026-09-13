cmake_minimum_required(VERSION 3.8)
project(cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)

add_executable(number_counter src/number_counter)
ament_target_dependencies(number_counter rclcpp example_interfaces)

add_executable(number_publisher src/number_publisher)
ament_target_dependencies(number_publisher rclcpp example_interfaces)

install(TARGETS 
  number_counter
  number_publisher
  DESTINATION lib/${PROJECT_NAME})

ament_package()
