Place these scripts in `/etc/sysconfig/network-scripts` on your
RedHat/CentOS/Fedora system.

Sample configuration for a `macvlan` interface:

    DEVICE=em1p0
    DEVICETYPE=macvlan
    TYPE=macvlan
    BOOTPROTO=none
    ONBOOT=yes
    NM_CONTROLLED=no

    MACVLAN_PARENT=em1
    MACVLAN_MODE=bridge

- `TYPE` can be either `macvlan` or `macvtap`.
- `MACVLAN_PARENT` is the name of the physical interface with which
  this `macvlan` interface is associated.
- `MACVLAN_MODE` can be `private`, `bridge`, `vepa`, or `passthru`.
  See [this commit][1] for more information.

[1]: https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id=618e1b7482f7a8a4c6c6e8ccbe140e4c331df4e9
 
License
=======

initscripts-macvlan  
Copyright (C) 2014 Lars Kellogg-Stedman

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

