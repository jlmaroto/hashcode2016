var droneTest = function() {
	this.point = [10,10]
	this.distanceToPoint = function(point){
		var distance = 	Math.sqrt(Math.pow(this.point[0] - point[0],2)+Math.pow(this.point[1] - point[1],2))
		return Math.ceil(distance);
	}
	
	this.load = function(){
		
	}
}

dr = new droneTest()

console.log(dr.distanceToPoint([3,6]))