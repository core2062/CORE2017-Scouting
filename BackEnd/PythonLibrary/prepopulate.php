<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
		<title>CORE 2062 Scouting</title>
		<link rel="shortcut icon" href="favicon.ico" />
		<meta name="description" content="CORE 2062 Scouting Form">
    	<meta name="author" content="CORE2062">
    	<meta name="robots" content="noindex, nofollow">

		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css" integrity="sha256-t2/7smZfgrST4FS1DT0bs/KotCM74XlcqZN5Vu7xlrw=" crossorigin="anonymous" />

		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/css/foundation.min.css" integrity="sha256-NTds7atVCDeolLUzbcl45lx4gJYO+hNXCaX1wC2HQHc=" crossorigin="anonymous" />

		<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js" integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8=" crossorigin="anonymous"></script>

		<script src="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/foundation.min.js" integrity="sha256-KXypdIy75PPHsbEaVkrhBvlQg8XTQy8NvalzrIxMrco=" crossorigin="anonymous"></script>

		<script src="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/foundation/foundation.accordion.min.js" integrity="sha256-Sf8QyM10GIsdziOWIIfN7V/ah4iRxPt17tvNCHorXjc=" crossorigin="anonymous"></script>

		<script src="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/foundation/foundation.tab.min.js" integrity="sha256-Qyd0HGGzEOB/qkGWHkxliFbXHCjs2VRDm8mzHEwphzk=" crossorigin="anonymous"></script>

		<script src="https://cdnjs.cloudflare.com/ajax/libs/awesomplete/1.1.1/awesomplete.min.js" integrity="sha256-hQ2PYbQiQS3xeguwt5BS+AMzn5V5JJ0P1kQnuoXdTnk=" crossorigin="anonymous"></script>

		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/awesomplete/1.1.1/awesomplete.min.css" integrity="sha256-pMulKeKs7Hns5vhu0uluhawM68QSrKg/dFfttaXCKE8=" crossorigin="anonymous" />

		<script src="https://cdnjs.cloudflare.com/ajax/libs/parsley.js/2.6.2/parsley.min.js" integrity="sha256-QKOftzbqahZaXS2amOh27JacZ6TbmT4TmGxNo4Jue4Y=" crossorigin="anonymous"></script>

	</head>
	<body>
		<form name="main" id="form" action="COREDataEntry.py" method="post" data-parsley-validate>
			<div class="row">
				<div class="small-12 columns">
					<ul class="tabs show-for-medium-up" data-tab>
						<li class="tab-title active"><a href="#panel1">Match/Scout Info</a></li>
      					<li class="tab-title"><a href="#panel2">Autonomous Period</a></li>
      					<li class="tab-title"><a href="#panel3">Teleoperated Period</a></li>
      				</ul>
      				<dl class="accordion" data-accordion>
      					<dd class="accordion-navigation">
      					
      					<a href="#panel1" class="show-for-small-only">Match/Scout Info</a>
      						<div id="panel1" class="content active">
      							<div class="content-box section-box">
      								
      								<div class="row">
      									<div class="small-12 columns">
      										<label>Match Number: *
												<input name="MatchNumber" class="form-control" type="number" placeholder="1" value="<?php echo $_GET['match']; ?>" readonly/>
											</label>
										</div>
									</div>

									<div class="row">
										<div class="small-12 columns">
											<label>Team Number: *
												<input name="TeamNumber" class="form-control" value="<?php echo $_GET['team']; ?>" placeholder="2062" readonly/>
											</label>
										</div>
									</div>

									<div class="row">
										<div class="small-12 columns">
											<label>Scout Name: *
												<input name="ScoutName" placeholder="John Smith" required/>
											</label>
										</div>
									</div>									

								</div>
							</div>

							<a href="#panel2" class="show-for-small-only">Autonomous Period</a>
	        					<div id="panel2" class="content">
	        						<div class="content-box section-box">

      									<div class="row">
      										<fieldset class="large-6 columns">
      										<legend>Deliver Gear:</legend>
      										 	<input name="DeliverGearAuto" id="leftgear" value="LeftGearAuto" type="radio"><label for="leftgear">Left</label>
      										 	<input name="DeliverGearAuto" id="middlegear" value="MiddleGearAuto" type="radio"><label for="middlegear">Middle</label>
      										 	<input name="DeliverGearAuto" id="rightgear" value="RightGearAuto" type="radio"><label for="rightgear">Right</label>
       										 	<input name="DeliverGearAuto" id="nonegear" value="None" type="radio"><label for="nonegear">None</label>     										 
      										</fieldset>
      									</div>

      								<div class="row">
      									<fieldset class="large-6 columns">
      										<legend>Crossed Baseline:</legend>
      										 <input name="CrossedBaselineAuto" id="CrossedBaseline" type="checkbox"><label for="CrossedBaseline">Yes</label>
      									</fieldset>
      								</div>

      								<div class="row">
      									<fieldset class="large-6 columns">
      										<legend>Score Fuel:</legend>
      										 <input name="FuelAuto" id="FuelLowAuto" value="FuelLowAuto" type="radio"><label for="FuelLowAuto">Low Goal</label>
      										 <input name="FuelAuto" id="FuelHighAuto" value="FuelHighAuto" type="radio"><label for="FuelHighAuto">High Goal</label>	 
      									</fieldset>
      								</div>

      								<div class="row"> 
      									<fieldset class="large-6 columns">
      										<legend>Post Auto Pressure: *</legend>
      										<label>
      											<input type="tel" value="0" name="PressureAuto">
      										</label>
      									</fieldset>
      								</div>

      							</div>
      						</div>	




      					<a href="#panel3" class="show-for-small-only">Teleoperated Period</a>
      						<div id="panel3" class="content">
      							<div class="content-box section-box">
 
                   					<div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                          						<label>Fuel Cycles:</label>
                        							<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("FuelCycleCountTele").stepDown(1);' value='-'/>
                        							</div>  
                        							<div class="small-4 columns">
                           					 			<input required type="number" name="FuelCycleCountTele" id="FuelCycleCountTele" min="0" step="1" value ="0" required readonly>
                        							</div>
                        							<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("FuelCycleCountTele").stepUp(1);' value='+'/>
                        							</div>
                      						</div>
                   				 		</div>
                  					</div>



									<div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                          				<label>Gears Delivered:</label>
                        				<div class="small-4 columns">
                          					<input required type='button' class="button postfix" onclick='document.getElementById("GearsDeliveredTele").stepDown(1);' value='-'/>
                        				</div>  
                        				<div class="small-4 columns">
                           					 <input required type="number" name="GearsDeliveredTele" id="GearsDeliveredTele" min="0" step="1" value ="0" required readonly>
                        				</div>
                        				<div class="small-4 columns">
                          				<input required type='button' class="button postfix" onclick='document.getElementById("GearsDeliveredTele").stepUp(1);' value='+'/>
                        				</div>
                      				</div>
                   				 </div>
                  				</div>                					 
                  				

                   					<div class="row">
                   					 <fieldset>
                  					<legend>Gears Dropped:</legend>
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                          				<label>Gears Dropped at Peg:</label>
                        				<div class="small-4 columns">
                          					<input required type='button' class="button postfix" onclick='document.getElementById("GearsDroppedTele").stepDown(1);' value='-'/>
                        				</div>  
                        				<div class="small-4 columns">
                           					 <input required type="number" name="GearsDroppedTele" id="GearsDroppedTele" min="0" step="1" value ="0" required readonly>
                        				</div>
                        				<div class="small-4 columns">
                          				<input required type='button' class="button postfix" onclick='document.getElementById("GearsDroppedTele").stepUp(1);' value='+'/>
                        				</div>
                      				</div>
                   				 </div>
                   				 
                  				</div>  

                   					<div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                          				<label>Gears Lost In Transit:</label>
                        				<div class="small-4 columns">
                          					<input required type='button' class="button postfix" name='subtract' onclick='document.getElementById("GearsDroppedTransitTele").stepDown(1);' value='-'/>
                        				</div>  
                        				<div class="small-4 columns">
                           					 <input required type="number" name="GearsDroppedTransitTele" id="GearsDroppedTransitTele" min="0" step="1" value ="0" required readonly>
                        				</div>
                        				<div class="small-4 columns">
                          				<input required type='button' class="button postfix" name='add' onclick='document.getElementById("GearsDroppedTransitTele").stepUp(1);' value='+'/>
                        				</div>
                      				</div>
                   				 </div>
                  				</div> 

                   					<div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                          				<label>Gears Dropped at Feeder Station:</label>
                        				<div class="small-4 columns">
                          					<input required type='button' class="button postfix" name='subtract' onclick='document.getElementById("GearsDroppedFeederTele").stepDown(1);' value='-'/>
                        				</div>  
                        				<div class="small-4 columns">
                           					 <input required type="number" name="GearsDroppedFeederTele" id="GearsDroppedFeederTele" min="0" step="1" value ="0" required readonly>
                        				</div>
                        				<div class="small-4 columns">
                          				<input required type='button' class="button postfix" name='add' onclick='document.getElementById("GearsDroppedFeederTele").stepUp(1);' value='+'/>
                        				</div>
                      				</div>
                   				 </div>
                  				</div>
                  				</fieldset>
                  				

      							<div class="row">
      									<fieldset class="large-12 columns">

      										<legend>Gear Manipulation:</legend>

      										 <input name="GearFloorPickup" id="GearFloorPickup" type="checkbox"><label for="GearFloorPickup">Floor Pickup?</label>

      										<legend>Gear Handling Type:</legend>
      										 <input name="GearFloorPickupType" id="ActivePickup" value="Active" type="radio"><label for="ActivePickup">Active</label>
      										  <input name="GearFloorPickupType" id="PassivePickup" value="Passive" type="radio"><label for="PassivePickup">Passive</label>
      										  <input name="GearFloorPickupType" id="NoPickup" value="None" type="radio"><label for="NoPickup">None</label>
      									</fieldset>
      								</div>                  				

      							<div class="row">
      									<fieldset class="large-12 columns">

      										<legend>Fuel Pickup Style:</legend>

      										 <input name="FuelPickupHopper" id="FuelPickupHopper" type="checkbox"><label for="FuelPickupHopper">Hopper/Feeder</label>
      										 <input name="FuelPickupFloor" id="FuelPickupFloor" type="checkbox"><label for="FuelPickupFloor">Floor</label>
      									</fieldset>
      								</div>

								</div>
							

							<fieldset>
								<legend>Score Fuel:</legend>
								<div class="row">
									
									<input name="ShooterType" id="High" value="High" type="radio"><label for="High">High Goal</label>
									<input name="ShooterType" id="Low" value="Low" type="radio"><label for="Low">Low Goal</label>
									 <input name="ShooterType" id="None" value="None" type="radio"><label for="None">None</label>

								</div>
							</fieldset>


                  					<fieldset>
                  					<legend>High Goal:</legend>
                   					<div class="row">
      										<legend>Frequency:</legend>
      										 <input name="HighFrequency" id="Slow" value="Slow" type="radio"><label for="Slow">Slow</label>
      										 <input name="HighFrequency" id="Medium" value="Medium" type="radio"><label for="Medium">Medium</label>
      										 <input name="HighFrequency" id="Fast" value="Fast" type="radio"><label for="Fast">Fast</label>

      										 <legend>Accuracy:</legend>
      										 <input name="HighAccuracy" id="25" value="25" type="radio"><label for="25">25% or less</label>
      										 <input name="HighAccuracy" id="50" value="50" type="radio"><label for="50">About 50%</label>
      										 <input name="HighAccuracy" id="75" value="75" type="radio"><label for="75">75% or more</label>
      								</div>

      								<div class="row"> 
      										<legend>Post Match Alliance Pressure:</legend>
      										<label>
      											<input type="tel" name="HighAlliancePressure">
      										</label>
      								</div>

      									</fieldset>  
                      				
                   				 
                  				

       								<div class="row">
      									<fieldset class="large-6 columns">
      										<legend>Low Goal:</legend>
                          <legend> </legend>
                          <legend>Frequency:</legend>
      										 <input name="LowGoalFrequency" id="SlowLow" value="SlowLow" type="radio"><label for="SlowLow">Slow</label>
      										 <input name="LowGoalFrequency" id="FastLow" value="FastLow" type="radio"><label for="FastLow">Fast</label>	 
      									</fieldset>
      								</div>                 										      								

							
							 

							<fieldset>
								<legend>Climbing:</legend>
								<div class="row">
									
									<input name="Climb" id="DidClimb" value="DidClimb" type="radio"><label for="DidClimb">Sucessful Climb</label>
									<input name="Climb" id="NoClimb" value="NoClimb" type="radio"><label for="NoClimb">No Climb</label>
									 <input name="Climb" id="ClimbFail" value="ClimbFail" type="radio"><label for="ClimbFail">Failed Climb</label>

								</div>
							</fieldset>





							<input class="button round SubmitButton" type="submit" value="Submit">
							</form>

							
							</dl>
<script>
      $(document).foundation();
</script>
<script type="text/javascript">
  $('#form').parsley();
</script>

	</body>
</html>     												