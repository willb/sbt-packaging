%global do_bootstrap 1
%global pkg_rel 1
%global scala_version 2.10.3

Name:           sbt
Version:        0.13.0
Release:        %{pkg_rel}%{?dist}
Summary:        simple build tool for Scala and Java projects

License:        BSD
URL:            http://www.scala-sbt.org
Source0:        https://github.com/sbt/sbt/archive/v%{version}.tar.gz
%if %{do_bootstrap}
# include bootstrap libraries

%endif

BuildRequires:  scala
%if !%{do_bootstrap}
BuildRequires:  sbt
%endif

Requires:       scala

%description
sbt is the simple build tool for Scala and Java projects.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install


%files
%{_javadir}/sbt/ivy/0.13.0/jars/ivy.jar
# %{_javadir}/sbt/ivy/0.13.0/srcs/ivy-sources.jar
%{_javadir}/sbt/task-system/0.13.0/jars/task-system.jar
# %{_javadir}/sbt/task-system/0.13.0/srcs/task-system-sources.jar
%{_javadir}/sbt/compiler-interface/0.13.0/jars/compiler-interface-src.jar
%{_javadir}/sbt/compiler-interface/0.13.0/jars/compiler-interface-bin.jar
%{_javadir}/sbt/testing/0.13.0/jars/testing.jar
# %{_javadir}/sbt/testing/0.13.0/srcs/testing-sources.jar
%{_javadir}/sbt/command/0.13.0/jars/command.jar
# %{_javadir}/sbt/command/0.13.0/srcs/command-sources.jar
%{_javadir}/sbt/test-agent/0.13.0/jars/test-agent.jar
# %{_javadir}/sbt/test-agent/0.13.0/srcs/test-agent-sources.jar
%{_javadir}/sbt/launcher-interface/0.13.0/jars/launcher-interface.jar
# %{_javadir}/sbt/launcher-interface/0.13.0/srcs/launcher-interface-sources.jar
%{_javadir}/sbt/run/0.13.0/jars/run.jar
# %{_javadir}/sbt/run/0.13.0/srcs/run-sources.jar
%{_javadir}/sbt/compiler-ivy-integration/0.13.0/jars/compiler-ivy-integration.jar
# %{_javadir}/sbt/compiler-ivy-integration/0.13.0/srcs/compiler-ivy-integration-sources.jar
%{_javadir}/sbt/scripted-sbt/0.13.0/jars/scripted-sbt.jar
# %{_javadir}/sbt/scripted-sbt/0.13.0/srcs/scripted-sbt-sources.jar
%{_javadir}/sbt/launch-test/0.13.0/jars/launch-test.jar
# %{_javadir}/sbt/launch-test/0.13.0/srcs/launch-test-sources.jar
%{_javadir}/sbt/collections/0.13.0/jars/collections.jar
# %{_javadir}/sbt/collections/0.13.0/srcs/collections-sources.jar
%{_javadir}/sbt/persist/0.13.0/jars/persist.jar
# %{_javadir}/sbt/persist/0.13.0/srcs/persist-sources.jar
%{_javadir}/sbt/classfile/0.13.0/jars/classfile.jar
# %{_javadir}/sbt/classfile/0.13.0/srcs/classfile-sources.jar
%{_javadir}/sbt/control/0.13.0/jars/control.jar
# %{_javadir}/sbt/control/0.13.0/srcs/control-sources.jar
%{_javadir}/sbt/launcher/0.13.0/jars/launcher.jar
# %{_javadir}/sbt/launcher/0.13.0/srcs/launcher-sources.jar
%{_javadir}/sbt/apply-macro/0.13.0/jars/apply-macro.jar
# %{_javadir}/sbt/apply-macro/0.13.0/srcs/apply-macro-sources.jar
%{_javadir}/sbt/datatype-generator/0.13.0/jars/datatype-generator.jar
# %{_javadir}/sbt/datatype-generator/0.13.0/srcs/datatype-generator-sources.jar
%{_javadir}/sbt/interface/0.13.0/jars/interface.jar
# %{_javadir}/sbt/interface/0.13.0/srcs/interface-sources.jar
%{_javadir}/sbt/main-settings/0.13.0/jars/main-settings.jar
# %{_javadir}/sbt/main-settings/0.13.0/srcs/main-settings-sources.jar
# %{_javadir}/sbt/precompiled-2_9_2/0.13.0/jars/compiler-interface-bin.jar
# %{_javadir}/sbt/precompiled-2_9_2/0.13.0/srcs/precompiled-2_9_2-sources.jar
%{_javadir}/sbt/incremental-compiler/0.13.0/jars/incremental-compiler.jar
# %{_javadir}/sbt/incremental-compiler/0.13.0/srcs/incremental-compiler-sources.jar
%{_javadir}/sbt/precompiled-2_8_2/0.13.0/jars/compiler-interface-bin.jar
# %{_javadir}/sbt/precompiled-2_8_2/0.13.0/srcs/precompiled-2_8_2-sources.jar
%{_javadir}/sbt/cache/0.13.0/jars/cache.jar
# %{_javadir}/sbt/cache/0.13.0/srcs/cache-sources.jar
%{_javadir}/sbt/compiler-integration/0.13.0/jars/compiler-integration.jar
# %{_javadir}/sbt/compiler-integration/0.13.0/srcs/compiler-integration-sources.jar
%{_javadir}/sbt/api/0.13.0/jars/api.jar
# %{_javadir}/sbt/api/0.13.0/srcs/api-sources.jar
%{_javadir}/sbt/main/0.13.0/jars/main.jar
# %{_javadir}/sbt/main/0.13.0/srcs/main-sources.jar
%{_javadir}/sbt/classpath/0.13.0/jars/classpath.jar
# %{_javadir}/sbt/classpath/0.13.0/srcs/classpath-sources.jar
%{_javadir}/sbt/logging/0.13.0/jars/logging.jar
# %{_javadir}/sbt/logging/0.13.0/srcs/logging-sources.jar
%{_javadir}/sbt/compile/0.13.0/jars/compile.jar
# %{_javadir}/sbt/compile/0.13.0/srcs/compile-sources.jar
%{_javadir}/sbt/process/0.13.0/jars/process.jar
# %{_javadir}/sbt/process/0.13.0/srcs/process-sources.jar
%{_javadir}/sbt/actions/0.13.0/jars/actions.jar
# %{_javadir}/sbt/actions/0.13.0/srcs/actions-sources.jar
%{_javadir}/sbt/sbt-launch/0.13.0/jars/sbt-launch.jar
%{_javadir}/sbt/scripted-plugin/0.13.0/jars/scripted-plugin.jar
# %{_javadir}/sbt/scripted-plugin/0.13.0/srcs/scripted-plugin-sources.jar
%{_javadir}/sbt/tracking/0.13.0/jars/tracking.jar
# %{_javadir}/sbt/tracking/0.13.0/srcs/tracking-sources.jar
%{_javadir}/sbt/tasks/0.13.0/jars/tasks.jar
# %{_javadir}/sbt/tasks/0.13.0/srcs/tasks-sources.jar
%{_javadir}/sbt/completion/0.13.0/jars/completion.jar
# %{_javadir}/sbt/completion/0.13.0/srcs/completion-sources.jar
%{_javadir}/sbt/cross/0.13.0/jars/cross.jar
# %{_javadir}/sbt/cross/0.13.0/srcs/cross-sources.jar
%{_javadir}/sbt/relation/0.13.0/jars/relation.jar
# %{_javadir}/sbt/relation/0.13.0/srcs/relation-sources.jar
%{_javadir}/sbt/io/0.13.0/jars/io.jar
# %{_javadir}/sbt/io/0.13.0/srcs/io-sources.jar
%{_javadir}/sbt/sbt/0.13.0/jars/sbt.jar
# %{_javadir}/sbt/sbt/0.13.0/srcs/sbt-sources.jar
# %{_javadir}/sbt/precompiled-2_9_3/0.13.0/jars/compiler-interface-bin.jar
# %{_javadir}/sbt/precompiled-2_9_3/0.13.0/srcs/precompiled-2_9_3-sources.jar
%{_javadir}/sbt/scripted-framework/0.13.0/jars/scripted-framework.jar
# %{_javadir}/sbt/scripted-framework/0.13.0/srcs/scripted-framework-sources.jar


%doc



%changelog