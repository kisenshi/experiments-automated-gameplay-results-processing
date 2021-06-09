# Merge all Z5 and D5 resulting temp files into one. This temp files were 
# generated as a result of the work presented in "MAP-Elites to Generate a Team 
# of Agents that Elicits Diverse Automated Gameplay". Refer to it for further
# details.
#
# Copyright (C) 2021 Cristina Guerrero-Romero
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

for experiment in a b c d f g h
    do
        echo "python mergeTempJson.py Z5/config30Z1$experiment 125"
        python mergeTempJson.py Z5/config30Z1$experiment 125
    done

for experiment in a b c d e f g h i j
    do
        echo "python mergeTempJson.py D5/config30D0$experiment 100"
        python mergeTempJson.py D5/config30D0$experiment 100
    done