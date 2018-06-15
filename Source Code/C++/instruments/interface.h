//
// Created by Adair on 2018/6/15.
//
#include "vector"
#include "map"
#ifndef INSTRUMENTS_INTERFACE_H
#define INSTRUMENTS_INTERFACE_H

virtual class IConfigurable{
    virtual int setParameters();
    virtual int getParameters();
    int dumpParameters();
    int loadParameters();
    int quickSave();
    int quickLoad();

private:
    char quickSavePath[256];
};



struct XMLInstrument{
    char connectionString[256];
    char identifier[256];
    std::map<char[256],char[256]> config;
};

class XMLParser{
    XMLParser();
    ~XMLParser();
    static std::vector<XMLInstrument> parse(char* path);
};


#endif //INSTRUMENTS_INTERFACE_H
