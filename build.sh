#!/usr/bin/env bash

CHROOTS="fedora-27-x86_64 fedora-26-x86_64 epel-6-x86_64 epel-7-x86_64"

function clean()
{
    rm -rf ${WORKSPACE}/rpmbuild/
    rm -rf ${WORKSPACE}/stage/
}

function prep()
{
    mkdir -p ${WORKSPACE}/rpmbuild/SPECS
    mkdir -p ${WORKSPACE}/rpmbuild/SOURCES
    for x in ${CHROOTS}; do
        case ${x} in 
            fedora-27-x86_64)
                TGT="fc27"
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
        mkdir -p ${WORKSPACE}/stage/${TGT}
    done
}

function build_srpms()
{
    cp discord.spec ${WORKSPACE}/rpmbuild/SPECS/
    spectool -g -R ${WORKSPACE}/rpmbuild/SPECS/discord.spec
    rpmbuild -bs ${WORKSPACE}/rpmbuild/SPECS/discord.spec
}

function build_rpms()
{
for x in ${CHROOTS}; do
    mock -r ${x} rebuild /rpmbuild/SRPMS/*.src.rpm
done
}

function stage_rpms()
{
    for x in ${CHROOTS}; do
        case ${x} in 
            fedora-27-x86_64)
                TGT="fc27"
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
        cp /var/lib/mock/${x}/result/*.rpm ${WORKSPACE}/stage/${TGT}/
    done
}

clean
prep
build_srpms
build_rpms
stage_rpms
