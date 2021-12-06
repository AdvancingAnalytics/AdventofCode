using Microsoft.VisualStudio.TestTools.UnitTesting;
using AdventOfCode_3;
using System.IO;

namespace AdventOfCode_3_Tests
{
    [TestClass]
    public class SubBinaryDiagnosticTests
    {
        [TestMethod]
        public void GetSubDiagnostics_WhenUsingSampleData_ReturnCorrectGamma()
        {
            var diagnostics = File.ReadAllLines("../../../SampleData.txt");

            var calc = new SubBinaryDiagnostic();
            var result = calc.GetSubDiagnostics(diagnostics);
            Assert.AreEqual(22, result.GammaRate);
        }

        [TestMethod]
        public void GetSubDiagnostics_WhenUsingSampleData_ReturnCorrectEpsilon()
        {
            var diagnostics = File.ReadAllLines("../../../SampleData.txt");

            var calc = new SubBinaryDiagnostic();
            var result = calc.GetSubDiagnostics(diagnostics);
            Assert.AreEqual(9, result.EpsilonRate);
        }

        [TestMethod]
        public void GetSubDiagnostics_WhenUsingSampleData_ReturnCorrectGammaBinary()
        {
            var diagnostics = File.ReadAllLines("../../../SampleData.txt");

            var calc = new SubBinaryDiagnostic();
            var result = calc.GetSubDiagnostics(diagnostics);
            Assert.AreEqual("10110", result.GammaRateBinary);
        }

        [TestMethod]
        public void GetSubDiagnostics_WhenUsingSampleData_ReturnCorrectEpsilonBinary()
        {
            var diagnostics = File.ReadAllLines("../../../SampleData.txt");

            var calc = new SubBinaryDiagnostic();
            var result = calc.GetSubDiagnostics(diagnostics);
            Assert.AreEqual("01001", result.EpsilonRateBinary);
        }

        [TestMethod]
        public void GetSubDiagnostics_WhenUsingSampleData_ReturnCorrectOxygenBinary()
        {
            var diagnostics = File.ReadAllLines("../../../SampleData.txt");

            var calc = new SubBinaryDiagnostic();
            var result = calc.GetSubDiagnostics(diagnostics);
            Assert.AreEqual("10111", result.OxygenBinary);
        }

        [TestMethod]
        public void GetSubDiagnostics_WhenUsingSampleData_ReturnCorrectCO2ScrubberBinary()
        {
            var diagnostics = File.ReadAllLines("../../../SampleData.txt");

            var calc = new SubBinaryDiagnostic();
            var result = calc.GetSubDiagnostics(diagnostics);
            Assert.AreEqual("01010", result.CO2ScrubberBinary);
        }
    }
}
