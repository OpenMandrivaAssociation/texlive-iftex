# revision 18833
# category Package
# catalog-ctan /macros/latex/contrib/iftex
# catalog-date 2010-06-08 10:18:35 +0200
# catalog-license lppl1.3
# catalog-version 0.2
Name:		texlive-iftex
Version:	0.2
Release:	3
Summary:	Am I running under pdfTeX, XeTeX or LuaTeX?
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/iftex
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iftex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iftex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package, which works both for Plain TeX and for LaTeX,
defines the \ifPDFTeX, \ifXeTeX, and \ifLuaTeX conditionals for
testing which engine is being used for typesetting. The package
also provides the \RequirePDFTeX, \RequireXeTeX, and
\RequireLuaTeX commands which throw an error if pdfTeX, XeTeX
or LuaTeX (respectively) is not the engine in use.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/iftex/iftex.sty
%doc %{_texmfdistdir}/doc/generic/iftex/README
%doc %{_texmfdistdir}/doc/generic/iftex/iftex.pdf
%doc %{_texmfdistdir}/doc/generic/iftex/iftex.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 752726
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 718704
- texlive-iftex
- texlive-iftex
- texlive-iftex
- texlive-iftex

