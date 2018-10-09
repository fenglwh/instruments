#include "visatype.h"
#include "visa.h"
#include <stdarg.h>
#include "vector"
#include "map"
#include "stdlib.h"

class CRemote
{
public:

    CRemote();
    ~CRemote();
//    std::vector<char[256]> listResource();
    int Open(char * lpsession);

    int Write(char * command);
    int Read(ViBuf retVal , unsigned int nBufCount);
    int Query(char * command,ViBuf retVal, unsigned int nBufCount);
    int Close();

private:
	int OpenDM();
	static bool DMOpend;
    ViSession m_viSession;
    ViStatus  m_ViStatus;
    ViSession m_vistr;
};








