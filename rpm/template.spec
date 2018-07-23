Name:           ros-indigo-kdl-parser-py
Version:        1.11.15
Release:        0%{?dist}
Summary:        ROS kdl_parser_py package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/kdl_parser_py
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-orocos-kdl >= 1.3.0
Requires:       ros-indigo-python-orocos-kdl
Requires:       ros-indigo-urdf
Requires:       ros-indigo-urdfdom-py
BuildRequires:  python-catkin_pkg
BuildRequires:  ros-indigo-catkin >= 0.5.68
BuildRequires:  ros-indigo-orocos-kdl >= 1.3.0
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-urdf

%description
The Kinematics and Dynamics Library (KDL) defines a tree structure to represent
the kinematic and dynamic parameters of a robot mechanism. kdl_parser_py
provides Python tools to construct a KDL tree from an XML robot representation
in URDF.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Jul 23 2018 Chris Lalancette <clalancette@osrfoundation.org> - 1.11.15-0
- Autogenerated by Bloom

* Wed May 17 2017 Chris Lalancette <clalancette@osrfoundation.org> - 1.11.14-0
- Autogenerated by Bloom

