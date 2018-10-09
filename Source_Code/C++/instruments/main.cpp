#include <iostream>
#include "remote.h"
#include "string.h"
int main() {
	CRemote a = CRemote();
	std::string st;
	std::cout<<a.Open("GPIB0::17::INSTR")<<std::endl;
	unsigned char retVal[256] = {};
	std::cout << a.Query("*IDN?", retVal, 256) << std::endl;
    std::cout << retVal << std::endl;
	std::cin.get();
    return 0;
}