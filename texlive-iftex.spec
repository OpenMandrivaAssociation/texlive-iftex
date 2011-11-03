# revision 18833
# category Package
# catalog-ctan /macros/latex/contrib/iftex
# catalog-date 2010-06-08 10:18:35 +0200
# catalog-license lppl1.3
# catalog-version 0.2
Name:		texlive-iftex
Version:	0.2
Release:	1
Summary:	Am I running under pdfTeX, XeTeX or LuaTeX?
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/iftex
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iftex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iftex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package, which works both for Plain TeX and for LaTeX,
defines the \ifPDFTeX, \ifXeTeX, and \ifLuaTeX conditionals for
testing which engine is being used for typesetting. The package
also provides the \RequirePDFTeX, \RequireXeTeX, and
\RequireLuaTeX commands which throw an error if pdfTeX, XeTeX
or LuaTeX (respectively) is not the engine in use.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/iftex/iftex.sty
%doc %{_texmfdistdir}/doc/generic/iftex/README
%doc %{_texmfdistdir}/doc/generic/iftex/iftex.pdf
%doc %{_texmfdistdir}/doc/generic/iftex/iftex.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
