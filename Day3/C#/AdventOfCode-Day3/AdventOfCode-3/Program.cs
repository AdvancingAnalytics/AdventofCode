using System;
using System.IO;

namespace AdventOfCode_3
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Calculating Submarine Location");

            var lines = File.ReadAllLines("puzzleinput2.txt");
            var subDiagnosticsCalculator = new SubBinaryDiagnostic();

            var puzzle1Result = subDiagnosticsCalculator.GetSubDiagnostics(lines);            
            var puzzle1Value = puzzle1Result.EpsilonRate * puzzle1Result.GammaRate;
            Console.WriteLine($"Puzzle 1 calculated value is: {puzzle1Value}");

            var puzzle2Value = puzzle1Result.CO2ScrubberRate * puzzle1Result.OxygenRate;
            Console.WriteLine($"Puzzle 2 calculated value is: {puzzle2Value}");
        }
    }
}
