TEMPLATE = app
QMAKE_CXXFLAGS+=-W -Wall -O3 -static -DHAVE_INLINE -DGSL_RANGE_CHECK_OFF -Isrc  -fpermissive
SOURCES += src/alignment_xmfa.cpp \
 src/alignment_structure.cpp \
 src/alignment.cpp \
 src/boot.cpp \
 src/burst.cpp \
 src/consensus.cpp \
 src/genes.cpp \
 src/hashcell.cpp \
 src/move_ages.cpp \
 src/move_delta.cpp \
 src/move_gap.cpp \
 src/move_hidden.cpp \
 src/move_hidden2.cpp \
 src/move_mu.cpp \
 src/move_nu.cpp \
 src/move_rho.cpp \
 src/move_wb.cpp \
 src/move.cpp \
 src/param.cpp \
 src/recorder.cpp \
 src/tree_coal.cpp \
 src/tree_simple.cpp \
 src/tree_upgma.cpp \
 src/tree_newick.cpp \
 src/tree.cpp \
 src/util.cpp \
 src/ClonalFrame.cpp
HEADERS += src/alignment_xmfa.h \
 src/alignment_structure.h \
 src/alignment.h \
 src/boot.h \
 src/burst.h \
 src/consensus.h \
 src/genes.h \
 src/hashcell.h \
 src/move_ages.h \
 src/move_delta.h \
 src/move_gap.h \
 src/move_hidden.h \
 src/move_hidden2.h \
 src/move_mu.h \
 src/move_nu.h \
 src/move_rho.h \
 src/move_wb.h \
 src/move.h \
 src/param.h \
 src/recorder.h \
 src/timeval.h \
 src/tree_coal.h \
 src/tree_simple.h \
 src/tree_upgma.h \
 src/tree_newick.h \
 src/tree.h \
 src/util.h
DESTDIR = bin
UI_DIR = build
LIBS = -lgsl -lgslcblas
MOC_DIR = build
OBJECTS_DIR = build
CONFIG += release
