import React from "react";

class FinalGradeCalculator extends React.Component
{
    constructor(props) {
        super(props);
        this.state = {
        curGrade: 0,
        desiredGrade: 0,
        finalWeight: 0,
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        const target = event.target;
        const value = +target.value;
        const name = target.name;

        this.setState({[name]: value});
    }

    handleSubmit(event) {
        const curGrade = this.state.curGrade;
        const desiredGrade = this.state.desiredGrade;
        const finalWeight = this.state.finalWeight / 100;
        let gradeNeeded = ( desiredGrade  -  curGrade * (1-finalWeight) )  /  finalWeight;
        alert('curGrade = ' + curGrade + '\ndesiredGrade = ' + desiredGrade + '\nfinalWeight = ' + finalWeight + "\ngradeNeeded = " + gradeNeeded);
        event.preventDefault();
    }

    render() {
        return (
        <div>
            {/* Input for current grade. */}
            <form>
            <label>
                Current Grade:
                <input 
                name="curGrade"
                type="number"
                value={this.state.curGrade}
                onChange={this.handleChange}
                />
            </label>
            </form>

            {/* Input for desired grade. */}
            <form>
            <label>
                Desired Grade:
                <input 
                name="desiredGrade"
                type="number"
                value={this.state.desiredGrade}
                onChange={this.handleChange}
                />
            </label>
            </form>

            {/* Input for exam weight. */}
            <form>
            <label>
                Final Exam Weight (%):
                <input 
                name="finalWeight"
                type="number"
                value={this.state.finalWeight}
                onChange={this.handleChange}
                />
            </label>
            </form>

            {/* Submit */}
            <form name="submit" onSubmit={this.handleSubmit}>
            <input type="submit" value="Calculate Answer" />
            </form>
        </div>
        )
    }
}

export default FinalGradeCalculator;