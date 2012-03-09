%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             bean-validation-api
Version:          1.0.0
Release:          4%{dist}
Summary:          Bean Validation API
Group:            Development/Libraries
License:          ASL 2.0
URL:              http://www.hibernate.org/subprojects/validator.html

# svn export http://anonsvn.jboss.org/repos/hibernate/beanvalidation/api/tags/v1_0_0_GA/ bean-validation-api-1.0.0.GA
# tar czf bean-validation-api-1.0.0.GA-src-svn.tar.gz bean-validation-api-1.0.0.GA
Source0:          %{name}-%{namedversion}-src-svn.tar.gz

BuildRequires:    java-devel
BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-provider-junit

Requires:         jpackage-utils
Requires:         java
BuildArch:        noarch

%description
This package contains Bean Validation (JSR-303) API

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Libraries
Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/validation-api-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc license.txt

%files javadoc
%{_javadocdir}/%{name}
%doc license.txt

%changelog
* Fri Mar 09 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.0-4
- Relocated jars to _javadir

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 29 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-2
- Added license file to distribution

* Tue Aug 16 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-1
- Initial packaging

