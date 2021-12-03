using System;

namespace AdventOfCode_2_1
{
    public class SubLocation
    {
        public int Horizontal { get; set; }
        public int Depth { get; set; }
    }

    public class SubLocationWithAim : SubLocation
    {
        public int Aim { get; set;}
    }
}