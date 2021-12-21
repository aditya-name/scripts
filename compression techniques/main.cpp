#include <string>
#include <core/global_definitions.hpp>
#include <core/base_column.hpp>
#include <core/column_base_typed.hpp>
#include <core/column.hpp>
#include <core/compressed_column.hpp>
#include <compression/dictionary_compressed_column.hpp>
#include <compression/delta_coding_compressed_column.hpp>
#include <compression/run_length_encoding.hpp>
#include  "unittest.hpp"

using namespace CoGaDB;

int main(){
	
            std::cout <<"---------- Delta: ---------- "<< std::endl;
	if(!unittest<DeltaCodingCompressedColumn, int>()){
		std::cout << "At least one Unittest Failed!" << std::endl;	
		return -1;	
	}
	std::cout << "----- Unitests Passed for Delta! ---------- " << std::endl;

	
 std::cout <<"---------- Dictionary: ---------- "<< std::endl;
	if(!unittest<DictionaryCompressedColumn ,std::string>()){
		std::cout << "At least one Unittest Failed!" << std::endl;	
		return -1;	
	}
	std::cout << "----------  Unitests Passed for Dictionary ! ---------- " << std::endl;
	
 std::cout <<"---------- RunLength: ---------- "<< std::endl;
	if(!unittest<RunLengthEncoding ,std::string>()){
		std::cout << "At least one Unittest Failed!" << std::endl;	
		return -1;	
	}
	std::cout << "----------  Unitests Passed for RunLength ! ---------- " << std::endl;

 return 0;
}


