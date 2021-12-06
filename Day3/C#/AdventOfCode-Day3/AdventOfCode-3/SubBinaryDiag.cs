using System;

namespace AdventOfCode_3
{
    public class SubBinaryDiag
    {
        public int GammaRate { 
            get {
                return Convert.ToInt32(GammaRateBinary, 2);
            }
        }        
        public int EpsilonRate {
            get {
                return Convert.ToInt32(EpsilonRateBinary, 2);
            }
        }

        public int OxygenRate { 
            get {
                return Convert.ToInt32(OxygenBinary, 2);
            }
        }        
        public int CO2ScrubberRate {
            get {
                return Convert.ToInt32(CO2ScrubberBinary, 2);
            }
        }

        public string GammaRateBinary { get; set; }
        public string EpsilonRateBinary { get; set; }
        public string CO2ScrubberBinary { get; set; }
        public string OxygenBinary { get; set; }
    }
}