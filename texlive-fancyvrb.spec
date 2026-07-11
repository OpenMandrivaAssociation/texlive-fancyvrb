%global tl_name fancyvrb
%global tl_revision 78721

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.6a
Release:	%{tl_revision}.1
Summary:	Sophisticated verbatim text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fancyvrb
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyvrb.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyvrb.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Flexible handling of verbatim text including: verbatim commands in
footnotes; a variety of verbatim environments with many parameters;
ability to define new customized verbatim environments; save and restore
verbatim text and environments; write and read files in verbatim mode;
build "example" environments (showing both result and verbatim source).

