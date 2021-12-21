
HEADER_FILES := $(wildcard */*.hpp)

all: main

main: base_column.cpp  main.cpp  ${HEADER_FILES}
	g++ -Wall -Wextra -Weffc++ -Werror -I. main.cpp base_column.cpp -o main -lboost_serialization

run:
	./main

documentation:
	cd doc; doxygen doxygen.conf

view_documentation:
	chrome doc/documentation/index.htm



