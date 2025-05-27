Name:		texlive-iftex
Version:	73115
Release:	1
Summary:	Am I running under pdfTeX, XeTeX or LuaTeX?
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/iftex
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iftex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iftex.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/generic/iftex
%doc %{_texmfdistdir}/doc/generic/iftex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
