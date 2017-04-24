$(function() {
    $('#HighFieldset').hide();
    $('#LowFieldset').hide();
    $('#PostAutoPressure').hide();
    $('#AutoGearStatus').hide();
});
function EnableAutoGearStatus() {
    $('#AutoGearStatus').show();
}
function DisableAutoGearStatus() {
    $('#AutoGearStatus').hide();
}
function HighGoal() {
    $('#HighFieldset').show();
    $('#LowFieldset').hide();
}
function LowGoal() {
    $('#HighFieldset').hide();
    $('#LowFieldset').show();
}
function BothDisabled() {
    $('#HighFieldset').hide();
    $('#LowFieldset').hide();
}
function DisableAutoPressure() {
    $('#PostAutoPressure').hide();

}
function EnableAutoPressure() {
    $('#PostAutoPressure').show();
}