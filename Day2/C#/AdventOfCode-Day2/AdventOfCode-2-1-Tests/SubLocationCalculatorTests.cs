using Microsoft.VisualStudio.TestTools.UnitTesting;
using AdventOfCode_2_1;
using System.IO;

namespace AdventOfCode_2_1_Tests
{
    [TestClass]
    public class SubLocationCalculatorTests
    {
        [TestMethod]
        public void GetSubLocation_WhenUsingSampleData_ReturnsCorrectDepth()
        {            
            var lines = File.ReadAllLines("../../../SampleData.txt");

            var calc = new SubLocationCalculator();
            var result = calc.GetSubLocation(lines);
            Assert.AreEqual(10, result.Depth);
        }

        [TestMethod]
        public void GetSubLocation_WhenUsingSampleData_ReturnsCorrectHorizontal()
        {
            var lines = File.ReadAllLines("../../../SampleData.txt");

            var calc = new SubLocationCalculator();
            var result = calc.GetSubLocation(lines);

            Assert.AreEqual(15, result.Horizontal);
        }        

        [TestMethod]
        public void GetSubLocationWithAim_WhenUsingSampleData_ReturnsCorrectDepth()
        {            
            var lines = File.ReadAllLines("../../../SampleData.txt");

            var calc = new SubLocationCalculator();
            var result = calc.GetSubLocationWithAim(lines);
            Assert.AreEqual(60, result.Depth);
        }

        [TestMethod]
        public void GetSubLocationWithAim_WhenUsingSampleData_ReturnsCorrectHorizontal()
        {
            var lines = File.ReadAllLines("../../../SampleData.txt");

            var calc = new SubLocationCalculator();
            var result = calc.GetSubLocationWithAim(lines);

            Assert.AreEqual(15, result.Horizontal);
        }        
    }
}
