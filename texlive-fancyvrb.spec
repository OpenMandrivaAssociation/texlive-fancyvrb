Name:		texlive-fancyvrb
Version:	65585
Release:	1
Summary:	Sophisticated verbatim text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fancyvrb
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyvrb.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyvrb.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/fancyvrb
%doc %{_texmfdistdir}/doc/latex/fancyvrb

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
