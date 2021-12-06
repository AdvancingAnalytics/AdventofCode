using System;
using System.Collections.Generic;
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

            return binaryDiag;
        }

        public IEnumerable<string> GetSomething(IEnumerable<string> diagnostics, int position)
        {
            var binaryDiag = new SubBinaryDiag();
            List<string> filteredDiags = new List<string>();

            var numOfOnes = diagnostics.Where(d => d[position] == '1').Count();
            var numOfZeroes = diagnostics.Where(d => d[position] == '0').Count();                

            if (numOfZeroes > numOfOnes)
            {
                filteredDiags = diagnostics.Where(d => d[position] == '0').ToList<string>();
            }
            else
            {
                filteredDiags = diagnostics.Where(d => d[position] == '1').ToList<string>();                                   
            }

            if (filteredDiags.Count() != 1)
            {
                filteredDiags = GetSomething(filteredDiags).ToList();
            }                    

            return filteredDiags;            
        }
    }
}