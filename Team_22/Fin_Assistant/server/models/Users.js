
import mongoose from 'mongoose';

const UserSchema = new mongoose.Schema({
  email: { type: String, unique: true, required: true },
  passwordHash: { type: String, required: true },
  name: { type: String, default: 'User' },
  monthlyIncome: { type: Number, default: 0 },
  goals: { type: [String], default: [] },
}, { timestamps: true });

export default mongoose.model('User', UserSchema);
