//
// Created by Adair on 2018/6/15.
//
#include "remote.h"

CRemote::CRemote():m_viSession(0),m_ViStatus(0),m_vistr(0) {


}

CRemote::~CRemote() {

}

int CRemote::OpenDM() {
    return (VI_SUCCESS == viOpenDefaultRM(&m_viSession));
}

std::vector<char[256]> CRemote::listResource() {

}

int CRemote::Open(char *lpsession) {
    return (VI_SUCCESS == viOpen(m_viSession,lpsession,VI_NULL,VI_NULL,&m_vistr));
}

int CRemote::Write(char *command) {
    ViUInt32 iretcount = 0;
    bool bPass = 0 ;
    char* pBuffer = new char[260* 64];
    strcpy(pBuffer,command);
    bPass = (bool)viWrite(m_vistr,(ViBuf)pBuffer,(unsigned int)strlen(pBuffer),&iretcount);
    delete [] pBuffer;
    return (VI_SUCCESS == bPass);
}

int CRemote::Read(char *lpVisaString, unsigned int nBufCount) {
    ViUInt32 vicount = 0 ;
    return (VI_SUCCESS == viRead(m_vistr,(ViBuf)lpVisaString,nBufCount,&vicount));
}

int CRemote::Query(char *command, char *retVal, unsigned int nBufCount) {
    if (this->Write(command)){
        return this->Read(retVal,nBufCount);
    }
    else{
        return _VI_ERROR;
    }
}

int CRemote::Close() {
    return  viClose(m_vistr) && viClose(m_viSession);
}

