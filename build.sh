#!/bin/bash

CHROOTS="fedora-25-x86_64 fedora-26-x86_64 epel-6-x86_64 epel-7-x86_64"

function clean()
{
    rm -rf rpmbuild/
    rm -rf stage/
}

function prep()
{
    mkdir -p rpmbuild/SPECS
    mkdir -p rpmbuild/SOURCES
    for x in ${CHROOTS}; do
        case ${x} in 
            fedora-25-x86_64)
                TGT="fc25"
                ;;
            fedora-26-x86_64)
                TGT="fc26"
                ;;
            epel-6-x86_64)
                TGT="el6"
                ;;
            epel-7-x86_64)
                TGT="el7"
                ;;
        esac
        mkdir -p stage/${TGT}
    done
}

function build_srpms()
{
    cp discord.spec rpmbuild/SPECS/
    spectool -g -R rpmbuild/SPECS/discord.spec
    rpmbuild -bs rpmbuild/SPECS/discord.spec
}

function build_rpms()
{
    for x in ${CHROOTS}; do
        mock -r ${x} rebuild rpmbuild/SRPMS/*.src.rpm
    done
}

function stage_rpms()
{
    for x in ${CHROOTS}; do
        case ${x} in 
            fedora-25-x86_64)
                TGT="fc25"
                ;;
            fedora-26-x86_64)
                TGT="fc26"
                ;;
            epel-6-x86_64)
                TGT="el6"
                ;;
            epel-7-x86_64)
                TGT="el7"
                ;;
        esac
        cp /var/lib/mock/${x}/result/*.rpm stage/${TGT}/
    done
}

clean
prep
build_srpms
build_rpms