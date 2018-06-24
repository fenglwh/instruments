//
// Created by Adair on 2018/6/15.
//
#include "remote.h"
#include "iostream"
CRemote::CRemote():m_viSession(0),m_ViStatus(0),m_vistr(0) {


}

CRemote::~CRemote() {

}

int CRemote::OpenDM() {
    return (VI_SUCCESS == viOpenDefaultRM(&m_viSession));
}
// I found these things will cuz issues, then I toggled these line for further use
// std::vector<char[256]> CRemote::listResource() {
// 	std::vector<char[256]> retVal;
// 	return retVal;
// }

int CRemote::Open(char *lpsession) {
	this->OpenDM();
	return (VI_SUCCESS==viOpen(m_viSession, lpsession, VI_NULL, VI_NULL, &m_vistr));
}

int CRemote::Write(char *command) {
    ViUInt32 iretcount = 0;
    char pBuffer[16640] = {0};
    strcpy(pBuffer,command);
	if (command[strlen(command) - 1] != '\n') {
		strcat(command, "\n");
	}
    return (VI_SUCCESS == viWrite(m_vistr, (ViBuf)pBuffer, (unsigned int)strlen(pBuffer), &iretcount));
}

int CRemote::Read(ViBuf lpVisaString, unsigned int nBufCount) {
    ViUInt32 vicount = 0 ;
    return (VI_SUCCESS == viRead(m_vistr,lpVisaString,nBufCount,&vicount));
}

int CRemote::Query(char *command, ViBuf retVal, unsigned int nBufCount) {
	if (this->Write(command)) {
		return this->Read(retVal, nBufCount);
	}
	else {
		return _VI_ERROR;
	}
}

int CRemote::Close() {
    return  viClose(m_vistr) && viClose(m_viSession);
}

