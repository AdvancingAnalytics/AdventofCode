using System.Linq;

namespace AdventOfCode_3
{
    public class SubBinaryDiagnostic
    {
        public SubBinaryDiag GetSubDiagnostics(string[] diagnostics)
        {
            var binaryDiag = new SubBinaryDiag();

            var length = diagnostics.First().Length;

            for (int i = 0; i < length; i++)
            {
                var numOfOnes = diagnostics.Where(d => d[i] == '1').Count();
                var numOfZeroes = diagnostics.Where(d => d[i] == '0').Count();                

                if (numOfZeroes > numOfOnes)
                {
                    binaryDiag.GammaRateBinary += "0";                    
                    binaryDiag.EpsilonRateBinary += "1";                                        
                }
                else
                {
                    binaryDiag.GammaRateBinary += "1";                        
                    binaryDiag.EpsilonRateBinary += "0";
                }                    
            }

            binaryDiag.OxygenBinary = GetOxygen(diagnostics);
            binaryDiag.CO2ScrubberBinary = GetCO2Scrubber(diagnostics);

            return binaryDiag;
        }

        public string GetOxygen(string[] diagnostics)
        {
            var filteredDiags = diagnostics;

            var length = diagnostics.First().Length;

            for (int i = 0; i < length; i++)
            {
                var numOfOnes = filteredDiags.Where(d => d[i] == '1').Count();
                var numOfZeroes = filteredDiags.Where(d => d[i] == '0').Count();                

                if (numOfZeroes > numOfOnes)
                {
                    filteredDiags = filteredDiags.Where(d => d[i] == '0').ToArray();                                
                }
                else
                {
                    filteredDiags = filteredDiags.Where(d => d[i] == '1').ToArray();                                
                }

                if (filteredDiags.Count() == 1)                    
                    break;
            }

            return filteredDiags.First();
        }

        public string GetCO2Scrubber(string[] diagnostics)
        {
            var filteredDiags = diagnostics;

            var length = diagnostics.First().Length;

            for (int i = 0; i < length; i++)
            {
                var numOfOnes = filteredDiags.Where(d => d[i] == '1').Count();
                var numOfZeroes = filteredDiags.Where(d => d[i] == '0').Count();                

                if (numOfZeroes > numOfOnes)
                {
                    filteredDiags = filteredDiags.Where(d => d[i] == '1').ToArray();                                
                }
                else
                {
                    filteredDiags = filteredDiags.Where(d => d[i] == '0').ToArray();                                
                }

                if (filteredDiags.Count() == 1)                    
                    break;
            }

            return filteredDiags.First();
        }

        public string GetFilteredDiags(string[] diagnostics, string toCount)
        {
            var filteredDiags = diagnostics;

            var length = diagnostics.First().Length;

            for (int i = 0; i < length; i++)
            {
                var numOfOnes = filteredDiags.Where(d => d[i] == '1').Count();
                var numOfZeroes = filteredDiags.Where(d => d[i] == '0').Count();                

                if (numOfZeroes > numOfOnes)
                {
                    filteredDiags = filteredDiags.Where(d => d[i] == '1').ToArray();                                
                }
                else
                {
                    filteredDiags = filteredDiags.Where(d => d[i] == '0').ToArray();                                
                }

                if (filteredDiags.Count() == 1)                    
                    break;
            }

            return filteredDiags.First();
        }
    }
}