# Generate all the resulting MAP-Elites from the experiments corresponding
# to the work presented in "MAP-Elites to Generate a Team of Agents that Elicits 
# Diverse Automated Gameplay" in png format. Refer to this work for further
# information about this data.
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

echo "python mapElitesData.py B2"
python mapElitesData.py B2

echo "python mapElitesData.py B3"
python mapElitesData.py B3

echo "python mapElitesData.py S4"
python mapElitesData.py S4

for experiment in a b c d f g h
    do
        echo "python mapElitesData.py Z5/config30Z1$experiment 125"
        python mapElitesData.py Z5/config30Z1$experiment 125
    done

for experiment in a b c d e f g h i j
    do
        echo "python mapElitesData.py D5/config30D0$experiment 100"
        python mapElitesData.py D5/config30D0$experiment 100
    done