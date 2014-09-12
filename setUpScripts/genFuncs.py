#!/usr/bin/python

import shutil, os, argparse, sys, stat


class genHelper:
    @staticmethod
    def generateCompfileFull(outFileName, externalDirLoc, cc, cxx, outName, installDirName, installDirLoc, neededLibs):
        availableLibs = ["CPPITERTOOLS","CPPPROGUTILS","ZI_LIB","BOOST","R","BAMTOOLS","CPPCMS","MATHGL","ARMADILLO","MLPACK","LIBLINEAR","PEAR","CURL","GTKMM", "BIBSEQ", "BIBCPP", "CATCH"]
        neededLibs = map(lambda x:x.upper(), neededLibs)
        """@todo: Make some of these default to an envirnment CC and CXX and maybe even CXXFLAGS as well 
            @todo: Make availableLibs a more universal constant"""
        with open(outFileName, "w") as f:
            f.write("CC = {CC}\n".format(CC = cc))
            f.write("CXX = {CXX}\n".format(CXX = cxx))
            f.write("CXXOUTNAME = {NAME_OF_PROGRAM}\n".format(NAME_OF_PROGRAM = outName))
            f.write("CXXFLAGS = -std=c++11 -Wall\n")
            f.write("CXXOPT += -O2 -funroll-loops -DNDEBUG  \n")
            f.write("ifneq ($(shell uname -s),Darwin)\n")
            f.write("\tCXXOPT += -march=native -mtune=native\n" )
            f.write("endif\n")
            f.write("\n")
            f.write("#debug\n")
            f.write("CXXDEBUG = -g -gstabs+ \n")
            f.write("INSTALL_DIR={INSTALL_LOCATION}\n".format(INSTALL_LOCATION = os.path.join(installDirLoc,installDirName)))
            f.write("EXT_PATH=$(realpath {EXTERNAL})\n".format(EXTERNAL = externalDirLoc))
            f.write("SCRIPTS_DIR=$(realpath scripts)\n")
            f.write("\n")
            for lib in availableLibs:
                if lib in neededLibs:
                    f.write("USE_{LIB} = 1\n".format(LIB = lib))
                else:
                    f.write("USE_{LIB} = 0\n".format(LIB = lib))


    @staticmethod            
    def determineCC(args):
        defaultCC = "gcc-4.8"
        if not args.CC:
            eCC = os.getenv("CC")
            if(eCC):
                defaultCC =  eCC
        else:
            defaultCC = args.CC[0]
        return defaultCC
    @staticmethod
    def determineCXX(args):
        defaultCXX = "g++-4.8"
        if not args.CXX:
            eCXX = os.getenv("CXX")
            if  eCXX:
                defaultCXX = eCXX
        else:
            defaultCXX = args.CXX[0]
        return defaultCXX