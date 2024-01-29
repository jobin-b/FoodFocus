import React from "react";
import ProgBar from "./progbar";

export interface DailyTotalsProps {
    calorieMax: number,
    calorieTotal: number,
    proteinMax: number,
    proteinTotal: number,
    carbsMax: number,
    carbsTotal: number,
    co2percent: number,
}

const DailyTotals: React.FC<DailyTotalsProps> = (props) => {
    return (
      <div className="flex flex-col w-full">
        <h2 className="text-2xl">Today's Totals</h2>
        <ProgBar label={`Calories ${props.calorieTotal}/${props.calorieMax}`} percent={props.calorieTotal/props.calorieMax} />
        <ProgBar label={`Protein ${props.proteinTotal}g/${props.proteinMax}g`} percent={props.proteinTotal/props.proteinMax} />
        <ProgBar label={`Carbs ${props.carbsTotal}g/${props.carbsMax}g`} percent={props.carbsTotal/props.carbsMax} />
        <ProgBar label="CO2" percent={props.co2percent} />
      </div>
    )
}

export default DailyTotals
