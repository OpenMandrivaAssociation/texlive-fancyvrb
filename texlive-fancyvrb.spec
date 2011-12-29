# revision 18492
# category Package
# catalog-ctan /macros/latex/contrib/fancyvrb
# catalog-date 2010-05-25 20:13:54 +0200
# catalog-license lppl
# catalog-version 2.8
Name:		texlive-fancyvrb
Version:	2.8
Release:	1
Summary:	Sophisticated verbatim text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fancyvrb
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyvrb.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyvrb.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyvrb.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Flexible handling of verbatim text including: verbatim commands
in footnotes; a variety of verbatim environments with many
parameters; ability to define new customized verbatim
environments; save and restore verbatim text and environments;
write and read files in verbatim mode; build "example"
environments (showing both result and verbatim source).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fancyvrb/fancyvrb.sty
%{_texmfdistdir}/tex/latex/fancyvrb/fvrb-ex.sty
%{_texmfdistdir}/tex/latex/fancyvrb/hbaw.sty
%{_texmfdistdir}/tex/latex/fancyvrb/hcolor.sty
%doc %{_texmfdistdir}/doc/latex/fancyvrb/Changes
%doc %{_texmfdistdir}/doc/latex/fancyvrb/Makefile
%doc %{_texmfdistdir}/doc/latex/fancyvrb/README
%doc %{_texmfdistdir}/doc/latex/fancyvrb/README.contrib
%doc %{_texmfdistdir}/doc/latex/fancyvrb/fancyvrb.pdf
%doc %{_texmfdistdir}/doc/latex/fancyvrb/fvrb-ex.pdf
%doc %{_texmfdistdir}/doc/latex/fancyvrb/t-fvrbex.tex
#- source
%doc %{_texmfdistdir}/source/latex/fancyvrb/fancyvrb.dtx
%doc %{_texmfdistdir}/source/latex/fancyvrb/fancyvrb.ins
%doc %{_texmfdistdir}/source/latex/fancyvrb/fvrb-ex.dtx
%doc %{_texmfdistdir}/source/latex/fancyvrb/fvrb-ex.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
