function LowDisable() {
    document.getElementById("SlowLow").disabled = true;
    document.getElementById("FastLow").disabled = true;
    document.getElementById("Slow").removeAttribute("disabled");
    document.getElementById("Medium").removeAttribute("disabled");
    document.getElementById("Fast").removeAttribute("disabled");
    document.getElementById("25").removeAttribute("disabled");
    document.getElementById("50").removeAttribute("disabled");
    document.getElementById("75").removeAttribute("disabled");
    document.getElementById("HighAlliancePressure").removeAttribute("disabled");
}
function HighDisable() {
	document.getElementById("SlowLow").removeAttribute("disabled");
	document.getElementById("FastLow").removeAttribute("disabled");
    document.getElementById("Slow").disabled = true;
    document.getElementById("Medium").disabled = true;
    document.getElementById("Fast").disabled = true;
    document.getElementById("25").disabled = true;
    document.getElementById("50").disabled = true;
    document.getElementById("75").disabled = true;
    document.getElementById("HighAlliancePressure").disabled = true;

}
function BothDisabled() {
    document.getElementById("Slow").disabled = true;
    document.getElementById("Medium").disabled = true;
    document.getElementById("Fast").disabled = true;
    document.getElementById("25").disabled = true;
    document.getElementById("50").disabled = true;
    document.getElementById("75").disabled = true;
    document.getElementById("HighAlliancePressure").disabled = true;
    document.getElementById("FastLow").disabled = true;
    document.getElementById("SlowLow").disabled = true;
}
function DisableAutoPressure() {
    document.getElementById("PressureAuto").disabled = true;

}
function EnableAutoPressure() {
    document.getElementById("PressureAuto").removeAttribute("disabled");
}